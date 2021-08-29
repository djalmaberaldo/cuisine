import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Restaurant } from './../service/restaurant.model';
import { RestaurantService } from './../service/restaurants.service.component';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {

  restaurants: Restaurant[] = [];

  filterForm = new FormGroup({
    name_restaurant: new FormControl(''),
    name_cuisine: new FormControl(''),
    price: new FormControl(''),
    distance: new FormControl(''),
    customer_rating: new FormControl(''),
  });

  constructor(private restaurantService: RestaurantService) { }

  ngOnInit(): void {
    this.filterForm.valueChanges.subscribe(() => {
      this.searchRestaurants();
    });
    this.searchRestaurants();
  }

  searchRestaurants() {
    let filters =  this.filterForm.getRawValue();
    Object.keys(filters).forEach(key => {
      if(!filters[key]) {
        delete filters[key];
      }
    });

    this.restaurantService
      .query(filters).subscribe(
        (body: Restaurant[]) => {
          this.restaurants = body;
        },
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

}
