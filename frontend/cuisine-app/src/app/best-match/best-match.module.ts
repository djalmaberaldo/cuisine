import { BestMatchRoutingModule } from './best-match.route';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchPageComponent } from './search-page/search-page.component';

@NgModule({
  declarations: [SearchPageComponent],
  imports: [
    CommonModule,
    BestMatchRoutingModule
  ],
  exports: [SearchPageComponent]
})
export class BestMatchModule { }
