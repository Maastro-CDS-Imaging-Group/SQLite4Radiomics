import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PingService } from '../services/ping.service';

@Component({
  selector: 'app-loading-page',
  templateUrl: './loading-page.component.html',
  styleUrls: ['./loading-page.component.css']
})
export class LoadingPageComponent implements OnInit {

  constructor(private router: Router, private pingService: PingService) { }

  ngOnInit() {
    this.pingBackend('/ping');
  }

  pingBackend(value: string) {
    this.pingService.ping(value).subscribe(
      (result) => { this.router.navigate(['/home']); },
      (error) => { setTimeout(() => this.pingBackend(value), 2000); }
    );
  }

}
