import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Restaurant } from '../service/restaurant.model';
import { RestaurantService } from '../service/restaurants.service';

@Component({
  selector: 'app-restaurant-form',
  templateUrl: './restaurant-form.component.html',
  styleUrls: ['./restaurant-form.component.scss']
})
export class RestaurantFormComponent  {

   isUpdate = false;

  filterForm = new FormGroup({
    name_restaurant: new FormControl(''),
    name_cuisine: new FormControl(''),
    price: new FormControl(''),
    distance: new FormControl(''),
    restaurant_id: new FormControl(''),
    customer_rating: new FormControl('', [Validators.max(5)])
  });

  constructor(
    private restaurantService:RestaurantService, 
    private router: Router) { 
      let restaurant:Restaurant = this.router.getCurrentNavigation()?.extras.state?.restaurant;
      if (restaurant) {
         this.isUpdate = true;
         this.filterForm.patchValue({
           name_restaurant: restaurant.name_restaurant,
           name_cuisine: restaurant.name_cuisine,
           price: restaurant.price,
           distance: restaurant.distance,
           customer_rating: restaurant.customer_rating,
           restaurant_id: restaurant.restaurant_id
         });
      }    
    }
  

  submit() {
    if (this.isUpdate) {
      this.restaurantService.update(this.filterForm.value).subscribe(
        () => {
          alert('Restaurant Updated');
          this.router.navigate(['']);
        });
    } else {
      this.restaurantService.post(this.filterForm.value).subscribe(
        () => {
          alert('Restaurant Added');
          this.router.navigate(['']);
        });
    }

  }


}
