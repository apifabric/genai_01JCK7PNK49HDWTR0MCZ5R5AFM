import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Wood-card.component.html',
  styleUrls: ['./Wood-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Wood-card]': 'true'
  }
})

export class WoodCardComponent {


}