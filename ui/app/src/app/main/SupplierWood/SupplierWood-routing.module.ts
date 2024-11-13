import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierWoodHomeComponent } from './home/SupplierWood-home.component';
import { SupplierWoodNewComponent } from './new/SupplierWood-new.component';
import { SupplierWoodDetailComponent } from './detail/SupplierWood-detail.component';

const routes: Routes = [
  {path: '', component: SupplierWoodHomeComponent},
  { path: 'new', component: SupplierWoodNewComponent },
  { path: ':id', component: SupplierWoodDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SupplierWood-detail-permissions'
      }
    }
  }
];

export const SUPPLIERWOOD_MODULE_DECLARATIONS = [
    SupplierWoodHomeComponent,
    SupplierWoodNewComponent,
    SupplierWoodDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierWoodRoutingModule { }