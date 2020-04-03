import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatabaseBrowserComponent } from './database-browser.component';

describe('DatabaseBrowserComponent', () => {
  let component: DatabaseBrowserComponent;
  let fixture: ComponentFixture<DatabaseBrowserComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatabaseBrowserComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatabaseBrowserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
