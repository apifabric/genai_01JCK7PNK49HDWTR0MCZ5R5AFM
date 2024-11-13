import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'StoreInventory-new',
  templateUrl: './StoreInventory-new.component.html',
  styleUrls: ['./StoreInventory-new.component.scss']
})
export class StoreInventoryNewComponent {
  @ViewChild("StoreInventoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}