import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Restaurant } from './../service/restaurant.model';
import { RestaurantService } from '../service/restaurants.service';

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
    customer_rating: new FormControl('', [Validators.max(5)]),
  });

  constructor(private restaurantService: RestaurantService) { }

  ngOnInit(): void {
    this.filterForm.valueChanges.subscribe(() => {
      this.searchRestaurants();
    });
    this.searchRestaurants();
  }

  /**
   * Does the search of restaurants and sets them to restaurants
   */
  searchRestaurants(): void {
    this.restaurantService
      .query(this.buildListOfFilters())
      .subscribe(
        (body: Restaurant[]) => {
          this.restaurants = body;
        },
        (res: HttpErrorResponse) => console.log(res.message)
      );
  }

  /**
   * Get all the values from filter list and removes the not valid ones
   *
   * @returns the list of the filters
   */
  buildListOfFilters(): object {
    const filters =  this.filterForm.getRawValue();
    Object.keys(filters).forEach(key => {
      if (!filters[key]) {
        delete filters[key];
      }
    });

    return filters;
  }

}
