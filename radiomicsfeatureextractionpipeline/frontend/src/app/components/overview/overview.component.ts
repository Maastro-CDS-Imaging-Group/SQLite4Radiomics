import { Component, OnInit, AfterViewInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent implements AfterViewInit {

  private dataSource: MatTableDataSource<any>;

  @ViewChild(MatTable, { static: false }) table: MatTable<any>;
  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: false }) sort: MatSort;

  displayedColumns = [];

  constructor(private dataService: DataService) {
    this.dataSource = new MatTableDataSource();
   }

  ngAfterViewInit() {
    this.dataChange();
  }

  // filter data in the table based on a stirng value provided
  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

   // add data to table columns
   addColumns(): void {
    this.displayedColumns = Object.keys(this.dataSource.data[0]);
  }

  // reload paginator, sorting and the rendered rows
  refreshTableRender(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    this.table.renderRows();
  }

  // everytime a different table name is selected, refresh table
  dataChange(): void {
    this.dataService.getOverview().subscribe((result) => {
      this.dataSource.data = result;
      this.addColumns();
      this.refreshTableRender();
    });
  }

  // reload data
  refresh(): void {
    this.dataChange();
  }

}
