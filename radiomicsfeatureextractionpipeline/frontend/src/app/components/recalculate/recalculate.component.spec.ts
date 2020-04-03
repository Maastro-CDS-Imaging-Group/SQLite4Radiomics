/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { RecalculateComponent } from './recalculate.component';

describe('RecalculateComponent', () => {
  let component: RecalculateComponent;
  let fixture: ComponentFixture<RecalculateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecalculateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecalculateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
