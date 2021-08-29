import { Restaurant } from './restaurant.model';
import { HttpClient } from '@angular/common/http';
import { RestaurantService } from './restaurants.service';
import { Observable, of } from 'rxjs';

describe('RestaurantsService', () => {
  let service: RestaurantService;
  let httpClient: HttpClient;
  let httpClientMock;
  let restaurantResponse: Restaurant[] = [
    {
      distance: 10,
      price: 10,
      customer_rating: 4,
      name_cuisine: "Cuisine",
      name_restaurant: "Restaurant"
    }];

  beforeEach(() => {
    httpClientMock = {
      get: (): Observable<any> => of(restaurantResponse)
    };
    service = new RestaurantService(httpClient);
    localStorage.setItem('sso_token', 'sso_token');
  });

  it('should get the restaurants', () => {
    const httpPutSpy = spyOn(service, 'query').and.returnValue(of(restaurantResponse));

    service.query().subscribe(
      res => {
        expect(res).toEqual(restaurantResponse);
      });
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
