import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientesService } from '../services/clientes-service';

@Component({
  selector: 'app-clientes',
  standalone: true,
  imports: [CommonModule],   // <-- adicione aqui
  templateUrl: './clientes.html',
  styleUrls: ['./clientes.css']
})
export class ClientesComponent implements OnInit {
  clientesAtivos: any[] = [];
  clientesTodos: any[] = [];

  constructor(private clientesService: ClientesService) {}

  ngOnInit(): void {
    this.clientesService.listarAtivos().subscribe(data => this.clientesAtivos = data);
    this.clientesService.listarTodos().subscribe(data => this.clientesTodos = data);
  }

  ativar(id: number) {
    this.clientesService.ativarCliente(id).subscribe(resp => console.log('Ativado:', resp));
  }

  inativar(id: number) {
    this.clientesService.inativarCliente(id).subscribe(resp => console.log('Inativado:', resp));
  }
}
