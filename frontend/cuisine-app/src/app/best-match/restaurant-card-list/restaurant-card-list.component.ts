import { Component, Input, OnInit } from '@angular/core';
import { Restaurant } from '../service/restaurant.model';

@Component({
  selector: 'app-restaurant-card-list',
  templateUrl: './restaurant-card-list.component.html',
  styleUrls: ['./restaurant-card-list.component.scss']
})
export class RestaurantCardListComponent implements OnInit {

  @Input() restaurants:Restaurant[] = [];

  constructor() { }

  ngOnInit(): void {
  }

}
