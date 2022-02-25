import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Restaurant } from '../service/restaurant.model';
import { RestaurantService } from '../service/restaurants.service';

@Component({
  selector: 'app-restaurant-card-list',
  templateUrl: './restaurant-card-list.component.html',
  styleUrls: ['./restaurant-card-list.component.scss']
})
export class RestaurantCardListComponent {

  @Input() restaurants:Restaurant[] = [];

  constructor(
    private restaurantService:RestaurantService,
    private route: Router) { }

  deleteRestaurant(id: any) {
    this.restaurantService.delete(id).subscribe(
      () => alert("Restaurant removed"));
  }

  updateRestaurant(restaurant: any) {
    this.route.navigate(['update', restaurant.restaurant_id], {state: { restaurant: restaurant }});
  }
}
