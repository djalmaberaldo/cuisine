import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RestaurantFormComponent } from './restaurant-form/restaurant-form.component';
import { SearchPageComponent } from './search-page/search-page.component';

const routes: Routes = [
  {
    path: '',
    component: SearchPageComponent
  },
  {
    path: 'add',
    component: RestaurantFormComponent
  },
  {
    path: 'update/:id',
    component: RestaurantFormComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule]
})
export class BestMatchRoutingModule {}
