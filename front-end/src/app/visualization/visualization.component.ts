import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-visualization',
  templateUrl: './visualization.component.html',
  styleUrls: ['./visualization.component.css']
})

export class VisualizationComponent implements OnInit {

	lineplotForm;

	constructor(private formBuilder: FormBuilder) { 

		this.lineplotForm = this.formBuilder.group({
			x: '',
			y: ''
		});

	}

	ngOnInit(): void {
	}

	public submitLineplot(){
		console.log(this.lineplotForm.get('x').value);
		console.log(this.lineplotForm.get('y').value);
	}

}
