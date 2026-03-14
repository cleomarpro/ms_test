import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClientesService {
  private BASE_URL = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  listarAtivos(): Observable<any> {
    return this.http.get(`${this.BASE_URL}/clientes/`);
  }

  listarTodos(): Observable<any> {
    return this.http.get(`${this.BASE_URL}/clientes/`, { params: { todos_cliente: 'on' } });
  }

  ativarCliente(id: number): Observable<any> {
    return this.http.post(`${this.BASE_URL}/clientes/status/`, {
      id_cliente: id,
      status_cliente: 'ATIVO'
    });
  }

  inativarCliente(id: number): Observable<any> {
    return this.http.post(`${this.BASE_URL}/clientes/status/`, {
      id_cliente: id,
      status_cliente: 'INATIVO'
    });
  }
}
