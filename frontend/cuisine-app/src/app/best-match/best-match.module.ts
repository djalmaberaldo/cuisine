import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BestMatchRoutingModule } from './best-match.route';
import { SearchPageComponent } from './search-page/search-page.component';

@NgModule({
  declarations: [SearchPageComponent],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    BestMatchRoutingModule
  ],
  exports: [SearchPageComponent]
})
export class BestMatchModule { }
