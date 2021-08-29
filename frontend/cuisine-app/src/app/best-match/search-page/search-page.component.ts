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
    name: new FormControl(''),
    cuisine: new FormControl(''),
    price: new FormControl(''),
    distance: new FormControl(''),
    rating: new FormControl(''),
  });

  filterObject = {};
  constructor(private restaurantService: RestaurantService) { }

  ngOnInit(): void {
    this.filterForm.valueChanges.subscribe(() => {
      this.searchRestaurants();
    });
    this.searchRestaurants();
  }

  searchRestaurants() {
    this.restaurantService
      .query({
        'name_restaurant': this.filterForm.get('name')?.value
      }).subscribe(
        (body: Restaurant[]) => {
          this.restaurants = body;
        },
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

}
