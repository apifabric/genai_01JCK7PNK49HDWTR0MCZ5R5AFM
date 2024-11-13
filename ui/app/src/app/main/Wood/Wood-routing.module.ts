import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WoodHomeComponent } from './home/Wood-home.component';
import { WoodNewComponent } from './new/Wood-new.component';
import { WoodDetailComponent } from './detail/Wood-detail.component';

const routes: Routes = [
  {path: '', component: WoodHomeComponent},
  { path: 'new', component: WoodNewComponent },
  { path: ':id', component: WoodDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Wood-detail-permissions'
      }
    }
  },{
    path: ':wood_id/Inventory', loadChildren: () => import('../Inventory/Inventory.module').then(m => m.InventoryModule),
    data: {
        oPermission: {
            permissionId: 'Inventory-detail-permissions'
        }
    }
},{
    path: ':wood_id/StoreInventory', loadChildren: () => import('../StoreInventory/StoreInventory.module').then(m => m.StoreInventoryModule),
    data: {
        oPermission: {
            permissionId: 'StoreInventory-detail-permissions'
        }
    }
},{
    path: ':wood_id/SupplierWood', loadChildren: () => import('../SupplierWood/SupplierWood.module').then(m => m.SupplierWoodModule),
    data: {
        oPermission: {
            permissionId: 'SupplierWood-detail-permissions'
        }
    }
}
];

export const WOOD_MODULE_DECLARATIONS = [
    WoodHomeComponent,
    WoodNewComponent,
    WoodDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WoodRoutingModule { }