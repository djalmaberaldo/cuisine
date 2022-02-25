import { Component, EventEmitter, Input, Output } from '@angular/core';
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
  @Output() updateRestaurantList = new EventEmitter<Restaurant[]>();

  constructor(
    private restaurantService:RestaurantService,
    private route: Router) { }

  deleteRestaurant(id: any) {
    this.restaurantService.delete(id).subscribe(
      (restaurants: Restaurant[]) => {
        alert("Restaurant removed");
        this.updateRestaurantList.emit(restaurants);
      });
  }

  updateRestaurant(restaurant: Restaurant) {
    this.route.navigate(['update', restaurant.restaurant_id], {state: { restaurant: restaurant }});
  }
}
