import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { RestaurantService } from '../service/restaurants.service';

@Component({
  selector: 'app-restaurant-form',
  templateUrl: './restaurant-form.component.html',
  styleUrls: ['./restaurant-form.component.scss']
})
export class RestaurantFormComponent {

  filterForm = new FormGroup({
    name_restaurant: new FormControl(''),
    name_cuisine: new FormControl(''),
    price: new FormControl(''),
    distance: new FormControl(''),
    customer_rating: new FormControl('', [Validators.max(5)]),
  });

  constructor(private restaurantService:RestaurantService) { }

  submit(){}

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
