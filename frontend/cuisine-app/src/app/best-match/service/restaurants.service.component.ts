import { HttpClient, HttpResponse } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { SERVER_API_URL } from 'src/app/app.constants';
import { Restaurant } from './restaurant.model';

type EntityArrayResponseType = HttpResponse<Restaurant[]>;

@Injectable({ providedIn: 'root' })
export class MovieService {
  public resourceUrl = SERVER_API_URL + '/resource/search';

  constructor(protected http: HttpClient) {}

  query(req?: any): Observable<EntityArrayResponseType> {
    return this.http
      .get<Restaurant[]>(this.resourceUrl, { params: req, observe: 'response' });
  }

}
