import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SupplierWood-card.component.html',
  styleUrls: ['./SupplierWood-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SupplierWood-card]': 'true'
  }
})

export class SupplierWoodCardComponent {


}