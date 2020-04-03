import { PrioritySetterComponent } from './components/priority-setter/priority-setter.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { FlexLayoutModule } from '@angular/flex-layout';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';




// Angular material and animation imports
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatDatepickerModule } from "@angular/material/datepicker";
import { MatNativeDateModule } from "@angular/material";
import { MatMomentDateModule, MomentDateAdapter } from "@angular/material-moment-adapter";
import { MatSnackBarModule, MatSnackBarRef, MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';
import {MatListModule} from '@angular/material/list';




// Components
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { DatabaseBrowserComponent } from './components/database-browser/database-browser.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { OpenfileDialogComponent } from "./components/openfile-dialog/openfile-dialog.component";
import { OverviewComponent } from "./components/overview/overview.component";

// Services
import { DataService } from './services/data.service';
import { PingService } from './services/ping.service';

// Routing
import { AppRouteRoutes } from './app-route.routing';

// Other components
import { HelpDialogComponent } from './components/help-dialog/help-dialog.component';
import { ReInitializeComponent } from "./components/re-initialize/re-initialize.component";
import { DeleteCalculationComponent } from "./components/delete-calculation/delete-calculation.component";
import { DeleteCsvComponent } from "./components/delete-csv/delete-csv.component";
import { LoadingPageComponent } from './loading-page/loading-page.component';

// Snackbar component
import { RecalculateComponent } from './components/recalculate/recalculate.component';



@NgModule({
   declarations: [
      AppComponent,
      DatabaseBrowserComponent,
      HeaderComponent,
      FooterComponent,
      OpenfileDialogComponent,
      HelpDialogComponent,
      ReInitializeComponent,
      DeleteCalculationComponent,
      RecalculateComponent,
      PrioritySetterComponent,
      DeleteCalculationComponent,
      DeleteCsvComponent,
      OverviewComponent,
      LoadingPageComponent,
      MainComponent
   ],
   imports: [
      BrowserModule,
      BrowserAnimationsModule,
      MatButtonModule,
      MatToolbarModule,
      MatMenuModule,
      MatIconModule,
      MatCardModule,
      MatTableModule,
      FlexLayoutModule,
      MatSelectModule,
      FormsModule,
      ReactiveFormsModule,
      MatInputModule,
      MatPaginatorModule,
      MatSortModule,
      HttpClientModule,
      MatDialogModule,
      MatFormFieldModule,
      MatDatepickerModule,
      MatNativeDateModule,
      MatSnackBarModule,
      MatMomentDateModule,
      MatListModule,
      AppRouteRoutes
   ],
   entryComponents: [
      OpenfileDialogComponent,
      HelpDialogComponent,
      ReInitializeComponent,
      DeleteCalculationComponent,
      RecalculateComponent,
      PrioritySetterComponent,
      DeleteCsvComponent
   ],
   schemas: [
      CUSTOM_ELEMENTS_SCHEMA
   ],
   providers: [
      DataService,
      PingService
   ],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
