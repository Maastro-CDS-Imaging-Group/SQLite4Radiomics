/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { PingService } from './ping.service';

describe('Service: Ping', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PingService]
    });
  });

  it('should ...', inject([PingService], (service: PingService) => {
    expect(service).toBeTruthy();
  }));
});
