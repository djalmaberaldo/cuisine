import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchPageComponent } from './search-page.component';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';

describe('SearchPageComponent', () => {
  let component: SearchPageComponent;
  let fixture: ComponentFixture<SearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientModule, FormsModule, ReactiveFormsModule],
      declarations: [ SearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have 5 filters inside the page', () => {
    const debugElement: DebugElement = fixture.debugElement;
    const filters = debugElement.queryAll(By.css('.form-control'));
    expect(filters.length).toEqual(5);
  });
});
