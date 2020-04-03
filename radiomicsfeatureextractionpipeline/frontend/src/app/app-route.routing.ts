import { LoadingPageComponent } from './loading-page/loading-page.component';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';

const routes: Routes = [
  { path: '', component: LoadingPageComponent },
  { path: 'home', component: MainComponent },
];

export const AppRouteRoutes = RouterModule.forRoot(routes);
