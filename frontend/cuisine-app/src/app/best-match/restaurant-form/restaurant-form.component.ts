import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Cuisine } from '../service/restaurant.model';
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

  constructor(
    private restaurantService:RestaurantService, 
    private router: Router) { }

  submit() {
    this.restaurantService.post(this.filterForm.value).subscribe(
      () => {
        console.log('Restaurant Added');
        this.router.navigate(['']);
      })
  }


}
