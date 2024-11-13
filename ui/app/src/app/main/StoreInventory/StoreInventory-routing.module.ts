import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StoreInventoryHomeComponent } from './home/StoreInventory-home.component';
import { StoreInventoryNewComponent } from './new/StoreInventory-new.component';
import { StoreInventoryDetailComponent } from './detail/StoreInventory-detail.component';

const routes: Routes = [
  {path: '', component: StoreInventoryHomeComponent},
  { path: 'new', component: StoreInventoryNewComponent },
  { path: ':id', component: StoreInventoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'StoreInventory-detail-permissions'
      }
    }
  }
];

export const STOREINVENTORY_MODULE_DECLARATIONS = [
    StoreInventoryHomeComponent,
    StoreInventoryNewComponent,
    StoreInventoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StoreInventoryRoutingModule { }