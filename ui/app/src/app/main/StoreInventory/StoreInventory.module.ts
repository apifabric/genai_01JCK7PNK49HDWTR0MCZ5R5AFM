import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {STOREINVENTORY_MODULE_DECLARATIONS, StoreInventoryRoutingModule} from  './StoreInventory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    StoreInventoryRoutingModule
  ],
  declarations: STOREINVENTORY_MODULE_DECLARATIONS,
  exports: STOREINVENTORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class StoreInventoryModule { }