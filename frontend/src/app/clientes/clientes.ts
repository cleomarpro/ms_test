import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientesService } from '../services/clientes-service';

@Component({
  selector: 'app-clientes',
  standalone: true,
  imports: [CommonModule],  
  templateUrl: './clientes.html',
  styleUrls: ['./clientes.css']
})
export class ClientesComponent implements OnInit {
  clientes: any[] = [];
  mostrarTodos = false;

  constructor(private clientesService: ClientesService) {}

  ngOnInit() {
    this.listarAtivos();
  }

  listarAtivos() {
    this.clientesService.listarAtivos().subscribe(data => {
      this.clientes = data;
      this.mostrarTodos = false;
    });
  }

  listarTodos() {
    this.clientesService.listarTodos().subscribe(data => {
      this.clientes = data;
      this.mostrarTodos = true;
    });
  }

  alternarStatus(cliente: any) {
  const novoStatus = cliente.status_cliente === 'ATIVO' ? 'INATIVO' : 'ATIVO';

  const confirmar = window.confirm(
    `Tem certeza que deseja alterar o status do cliente "${cliente.nome}" para ${novoStatus}?`
  );

  if (confirmar) {
    this.clientesService.atualizarStatus(cliente.id, novoStatus).subscribe(() => {
      // atualiza localmente para efeito imediato
      cliente.status_cliente = novoStatus;

      // recarrega a lista para garantir consistência com o backend
      if (this.mostrarTodos) {
        this.listarTodos();
      } else {
        this.listarAtivos();
      }
    });
  }
}

}
