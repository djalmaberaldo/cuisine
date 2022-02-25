import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { SERVER_API_URL } from 'src/app/app.constants';
import { Restaurant } from './restaurant.model';

@Injectable({ providedIn: 'root' })
export class RestaurantService {
  public resourceUrl = SERVER_API_URL + '/resource';

  constructor(protected http: HttpClient) {}

  /**
   * Does a get request to find the best restaurants based on the list of filters
   *
   * @param filters A object with valid filters
   * @returns Observable<Restaurant[]>
   */
  query(filters?: any): Observable<Restaurant[]> {
    return this.http
      .get<Restaurant[]>(this.resourceUrl+"/search", {params: filters});
  }

  /**
   * 
   * @param id 
   * @returns 
   */
  delete(id: number): Observable<any> {
    return this.http.delete(this.resourceUrl + "/delete/" + id);
  }

}
