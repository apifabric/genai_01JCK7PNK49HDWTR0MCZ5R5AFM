import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLIERWOOD_MODULE_DECLARATIONS, SupplierWoodRoutingModule} from  './SupplierWood-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplierWoodRoutingModule
  ],
  declarations: SUPPLIERWOOD_MODULE_DECLARATIONS,
  exports: SUPPLIERWOOD_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplierWoodModule { }