import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Restaurant } from './../service/restaurant.model';
import { RestaurantService } from './../service/restaurants.service.component';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {

  restaurants: Restaurant[] = [];
  searchRef: string = '';
  constructor(private restaurantService: RestaurantService) { }

  ngOnInit(): void {
    this.searchRestaurants();
  }

  searchRestaurants() {
    this.restaurantService
      .query({
        "customer_rating": 3,
        "price": 10
      })
      .subscribe(
        (body: Restaurant[]) => {
          this.restaurants = body;
        },
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

}
