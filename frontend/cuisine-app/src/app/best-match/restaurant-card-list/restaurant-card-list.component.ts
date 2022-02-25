import { Component, Input, OnInit } from '@angular/core';
import { Restaurant } from '../service/restaurant.model';
import { RestaurantService } from '../service/restaurants.service';

@Component({
  selector: 'app-restaurant-card-list',
  templateUrl: './restaurant-card-list.component.html',
  styleUrls: ['./restaurant-card-list.component.scss']
})
export class RestaurantCardListComponent {

  @Input() restaurants:Restaurant[] = [];

  constructor(private restaurantService:RestaurantService) { }

  deleteRestaurant(id: any) {
    this.restaurantService.delete(id).subscribe(
      () => console.log("Restaurant removed"));
  }
}
