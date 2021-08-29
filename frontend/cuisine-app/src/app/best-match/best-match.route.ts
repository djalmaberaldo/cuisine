import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { BestMatchModule } from "./best-match.module";
import { SearchPageComponent } from "./search-page/search-page.component";


const routes: Routes = [
  {
    path: '',
    component: SearchPageComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule]
})
export class BestMatchRoutingModule {}
