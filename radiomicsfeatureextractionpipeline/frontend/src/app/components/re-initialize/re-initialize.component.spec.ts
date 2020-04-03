/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { ReInitializeComponent } from './re-initialize.component';

describe('ReInitializeComponent', () => {
  let component: ReInitializeComponent;
  let fixture: ComponentFixture<ReInitializeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReInitializeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReInitializeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
