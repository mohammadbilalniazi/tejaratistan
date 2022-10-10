var data;
var selling_price_obj={}
function adding_row(){
    
    table_form=document.getElementById("table_form");
    row_elements=document.getElementById("row_elements");

    var list_tr=document.createElement("tr");
    var td_in_tr1=document.createElement("td");
    var div_in_td1=document.createElement("div");
    var div_in_div1=document.createElement("div");

    var select_item_name_in_div=document.createElement("select");
    select_item_name_in_div.id='item_name';
    select_item_name_in_div.name='item_name';
    select_item_name_in_div.required=true;
    product_id="all";
    url='/products/'+product_id+'/';
    fetch(url,{
        'method':'GET'
    }).then(response=>response.json()).then(data=>{
        //console.log(data);
        for(key in data){
            console.log(" data=",data)
            var option_in_select=document.createElement("option");
            //alert(data)
            option_in_select.value=data[key]['id'];
            option_in_select.innerText=data[key]['item_name'];
            select_item_name_in_div.appendChild(option_in_select);
            selling_price_obj[data[key]['id']]=data[key]['selling_price']
            //select_item_name_in_div.appendChild(option_in_select2)

        }
        //console.log("price_obj ",selling_price_obj)
    }).catch(e=>{
        console.log(e);
    })

    

    table_form.appendChild(list_tr);
    list_tr.appendChild(td_in_tr1);
    td_in_tr1.appendChild(div_in_td1);
    //div_in_div1.appendChild(div_in_div1);
    div_in_td1.appendChild(select_item_name_in_div);


    var item_amount_in_div=document.createElement("input");
    item_amount_in_div.type="number"
    item_amount_in_div.id='item_amount'
    item_amount_in_div.className='item_amount'
    item_amount_in_div.name='item_amount'
    item_amount_in_div.required=true;
    var td_in_tr2=document.createElement("td");
    var div_in_td2=document.createElement("div");
    //var div_in_div2=document.createElement("div");
    list_tr.appendChild(td_in_tr2)
    td_in_tr2.appendChild(div_in_td2)
    div_in_td2.appendChild(item_amount_in_div)
    var item_price_in_div=document.createElement("input");
    item_price_in_div.type="number"
    item_price_in_div.id='item_price'
    item_price_in_div.name='item_price'
    item_price_in_div.className='item_price'
    item_price_in_div.required=true;
    var td_in_tr2=document.createElement("td");
    var div_in_td2=document.createElement("div");
    list_tr.appendChild(td_in_tr2)
    td_in_tr2.appendChild(div_in_td2)
    div_in_td2.appendChild(item_price_in_div)
    var return_qty_in_div=document.createElement("input");
    return_qty_in_div.type="number"
    return_qty_in_div.id='return_qty'
    return_qty_in_div.name='return_qty'
    return_qty_in_div.required=true;
    var td_in_tr2=document.createElement("td");
    var div_in_td2=document.createElement("div");
    list_tr.appendChild(td_in_tr2)
    td_in_tr2.appendChild(div_in_td2)
    div_in_td2.appendChild(return_qty_in_div)

    //#######################now add events to created elements#########################
    item_amount=document.getElementsByClassName("item_amount");
    item_price=document.getElementsByClassName("item_price");
    for(i=0; i<item_amount.length; i++){
        item_amount[i].addEventListener("keyup",e=>{
            total_amount_bill();
        })

        item_price[i].addEventListener("keyup",e=>{
            total_amount_bill();
        })
    }
}


function purchase_bills(){
    var purchase_body=document.getElementById("purchase_body");
    alert("purchse bill");
    //console.log("purchase_body");
}


function purchase_form_submit(){
    var purchase_body=document.getElementById("purchase_body");
    alert("purchse bill");
    //console.log("purchase_body");
}

function total_amount_bill(){
    item_amount=document.getElementsByClassName("item_amount");
    item_price=document.getElementsByClassName("item_price");
    console.log("item_price=",item_price[0].value)
    total_bill_amount=document.getElementById("total_bill_amount");
    offset=0; 
    for(let i=0; i<item_amount.length; i++){
        if(item_amount[i].value!="" && item_price[i].value!=""){
            offset=offset+item_amount[i].value*item_price[i].value;
        }
    }
    console.log(offset)
    total_bill_amount.value=offset;
    // alert(item_amount)
}


// try{
   
// }
// catch{
//     console.log("no items");
// }



function select_vendors(){
    //alert("vendors")
    
    seller_span=document.getElementById("seller_span");
    //console.log("seller_span=",seller_span)
    seller_span.innerHTML="";
    var select_seller_in_div=document.createElement("select");
    select_seller_in_div.id='seller';
    select_seller_in_div.name='seller';
    select_seller_in_div.required=true;
    vendor_id="all";
    url='/vendors/'+vendor_id+'/';
    fetch(url,{
        'method':'GET'
    }).then(response=>response.json()).then(data=>{
        //alert(data.length)
        for(key in data){
            //console.log("key=",key," data[key]=",data[key])
            var option_in_select=document.createElement("option");
            option_in_select.value=data[key]['id'];
            option_in_select.innerText=data[key]['name'];
            select_seller_in_div.appendChild(option_in_select);
            //select_item_name_in_div.appendChild(option_in_select2)
        }
        seller_span.appendChild(select_seller_in_div);       
    }).catch(e=>{
        console.log(e);
    })

}


select_vendors();


// function validate_inputs(total_payment){
//     total_payment_input=document.getElementById("total_payment");
//     total_payment=total_payment_input.value;
//     alert("validate inputs");
//     total_bill_amount=document.getElementById("total_bill_amount").value;
//     if(total_payment>total_bill_amount){
//         total_payment_input.value="";
//     }
// }

// total_payment=document.getElementById("total_payment");
// total_payment.addEventListener("keyup",e=>{
//     validate_inputs();
// })