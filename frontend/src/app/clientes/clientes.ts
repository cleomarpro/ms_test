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

  ngOnInit(): void {
    // Ao carregar a página, já lista os ativos
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
  const ativo = cliente.status === 'ATIVO';
  const novoStatus = ativo ? 'INATIVO' : 'ATIVO';
  const acao = ativo ? 'Inativar' : 'Ativar';

  if (confirm(`Deseja ${acao} o cliente ${cliente.nome}?`)) {
    this.clientesService.atualizarStatus(cliente.id, novoStatus).subscribe({
      next: () => {
        alert(`Cliente ${cliente.nome} foi ${acao} com sucesso!`);

        // 🔄 Atualiza localmente e força refresh
        this.clientes = this.clientes.map(c =>
          c.id === cliente.id ? { ...c, status: novoStatus } : c
        );
      },
      error: (err) => {
        alert("Erro ao atualizar cliente: " + err.message);
      }
    });
  }
}


}
