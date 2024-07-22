{

    window.onload = function () {
        validateInputs();
    }

    // Function to validate Mileage
    function setMilleage(event) {       
        
        const startMileage = Number(document.getElementById("start_mileage").value)
        const endMileage = Number(document.getElementById("end_mileage").value)
        const totalMileage = document.getElementById("total_mileage")
        let   startMileageText = document.getElementById("start_mileage_text")
        let   endMileageText = document.getElementById("end_mileage_text")
        let savebtn = document.getElementById("save_btn");
        let result = false

        if ( startMileage!= 0 || endMileage != 0 )
        {
            if (endMileage <= startMileage)
            {
                startMileageText.innerHTML = "mileage must be smaller than ending mileage"
                endMileageText.innerHTML = "mileage must be greater than starting mileage" 
            }                                       

            if (startMileage <= 0 )
                startMileageText.innerHTML = "mileage must be greater than 0"

            if (endMileage <= 0 )
                endMileageText.innerHTML = "mileage must be greater than 0"   

            if ( startMileage > 0 && endMileage > 0 && endMileage > startMileage)
            {
                result = true
                startMileageText.innerHTML = "" 
                endMileageText.innerHTML = ""  
                totalMileage.value = (endMileage - startMileage ).toString()
            }
            else
                totalMileage.value = 0
                                                        
                                            
        }
        savebtn.disabled = !result 
    // setTime(result) 
                                                        
    }

    // Function to format text to hh24:mm:ss time format
    function num2time (num)
    {

        if (num < 100 && num > 0) num *=100;                                            
        
        let [_,hh,mm] = "0000"

        if (num > 0)
            [_,hh,mm] = num.toString().match(/(\d{1,2})(\d{2})$/)
            
                
        return `${hh.padStart(2,"0")}:${mm}`
    }

    // Function to validate if Time is Valid
    function setTime(event) {
                
        let startTime = document.getElementById("start_time")
        let startLunchTime = document.getElementById("start_lunch_time")
        let endLunchTime =  document.getElementById("end_lunch_time")
        let endTime = document.getElementById("end_time")
        let formStatus = false
        'use strict'
        let result = result2 = result3 = result4 = '' 

        if (event != null)
        {
            if (event.value > 0 && event.value < 100)
                event.value *=100
        }
    
        // Validate Time Format
        if (startTime.value != '')
            result = moment(num2time(startTime.value), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time')
        else 
            result = "Please fill out Clock In"


        if (endTime.value != '')
            result2 = moment(num2time(endTime.value), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time')
        else
            result2 = "Please fill out Clock Out"

        if (startLunchTime.value != '')    
            result3 = moment(num2time(startLunchTime.value), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time')

        if (endLunchTime.value != '')
            result4 = moment(num2time(endLunchTime.value), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time') 
        



        document.getElementById("start_time_text").innerHTML =  result
        document.getElementById("start_lunch_time_text").innerHTML =  result3
        document.getElementById("end_lunch_time_text").innerHTML =  result4
        document.getElementById("end_time_text").innerHTML =  result2

        if (result != 'Invalid Time' || result2 != 'Invalid Time' || result3 != 'Invalid Time' || result4 != 'Invalid Time')
            formStatus = true
        

        
        document.getElementById("save_btn").disabled = !formStatus
        console.log(!formStatus);

    
    }

    function validarCampos()
    {
        console.log("validando campos")
        setMilleage()
        setTime() 
    }




    function validateInputs(event) {

        if (event != null)
        {
            if (event.value > 0 && event.value < 100)
                event.value *=100
        }

        // Get input values
        let startTime = document.getElementById('start_time').value;
        let endTime = document.getElementById('end_time').value;
        let startLunchTime = document.getElementById('start_lunch_time').value;
        let endLunchTime = document.getElementById('end_lunch_time').value;
        
        let isValid = true;
        let result = '' 

       
    
        // Validate start time
        result = moment(num2time(startTime), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time');
        console.log('start',result);
        console.log(startTime);
        console.log(endTime);
        if ( startTime == ''   ) {
            isValid = false;
            document.getElementById("start_time_text").innerHTML = "Please fill Clock In field";
            document.getElementById("start_time_text").className = "error-text";
        }
        else if (result == 'Invalid Time')
        {
            isValid = false;
            document.getElementById("start_time_text").innerHTML = "Start time must be a valid Time Format";
            document.getElementById("start_time_text").className = "error-text";
        }
        else if (Number(startTime) >= Number(endTime))
            {
                isValid = false;
                document.getElementById("start_time_text").innerHTML = "Start time must be smaller than end Time";
                document.getElementById("start_time_text").className = "error-text";
            }
        else
        {
            document.getElementById("start_time_text").innerHTML = result;
            document.getElementById("start_time_text").className = "info-text";
        }

        
        // Validate end time
        result = moment(num2time(endTime), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time');
        console.log('end',result);
        console.log(startTime);
        console.log(endTime);
   
        if (endTime == '')  {
            isValid = false;
            document.getElementById("end_time_text").innerHTML = "Please fill Clock Out field";
            document.getElementById("end_time_text").className = "error-text";
        }
        else if (result == 'Invalid Time')
        {
            isValid = false;
            document.getElementById("end_time_text").innerHTML = "End time must be a valid Time Format";
            document.getElementById("end_time_text").className = "error-text";
        }
        else if (Number(endTime) <= Number(startTime))
        {
            isValid = false;
            document.getElementById("end_time_text").innerHTML = "End time must be greater than start time";
            document.getElementById("end_time_text").className = "error-text";
        }
        else
        {
            isValid = true;
            document.getElementById("end_time_text").innerHTML = result;
            document.getElementById("end_time_text").className = "info-text";
        }
    

        
        // Validate start lunch time if provided
       /* if (startLunchTime != '' || endLunchTime != '') {
            result = moment(num2time(startLunchTime), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time');
            console.log('start L',result);
            if (startLunchTime <= startTime || startLunchTime >= endTime) {
                isValid = false;
                document.getElementById("start_lunch_time_text").innerHTML = "start Lunch time must be a valid Time Format and greater than start time";
                document.getElementById("start_lunch_time_text").className = "error-text";
            }
            else
            {
                isValid = true;
                document.getElementById("start_lunch_time_text").innerHTML = result;
                document.getElementById("start_lunch_time_text").className = "info-text";
            }
    
            // Validate end lunch time if start lunch time is provided
            result = moment(num2time(endLunchTime), 'HH:mm:ss').format('h:mm:ss A').replace('Invalid date','Invalid Time');
            console.log('End L',result);
            if ( endLunchTime <= startTime || endLunchTime <= startLunchTime) {
                isValid = false;
                document.getElementById("end_lunch_time_text").innerHTML = "End time must be a valid Time Format and greater than start time";
                document.getElementById("end_lunch_time_text").className = "error-text";
            }
            else
            {
                isValid = true;
                document.getElementById("end_lunch_time_text").innerHTML = result;
                document.getElementById("end_lunch_time_text").className = "info-text";
            }

        }*/
        

        
        const startMileage = Number(document.getElementById("start_mileage").value)
        const endMileage = Number(document.getElementById("end_mileage").value)
        const totalMileage = document.getElementById("total_mileage")
        let   startMileageText = document.getElementById("start_mileage_text")
        let   endMileageText = document.getElementById("end_mileage_text")
        let savebtn = document.getElementById("save_btn");
       
        

        if ( startMileage!= 0 || endMileage != 0 )
        {
            if (endMileage <= startMileage)
            {
                isValid= false
                startMileageText.innerHTML = "mileage must be smaller than ending mileage"
                endMileageText.innerHTML = "mileage must be greater than starting mileage" 
            }       
            else
                isValid= true                                

            if (startMileage <= 0 )
            {
                isValid= false
                startMileageText.innerHTML = "mileage must be greater than 0"
            }                
            else
                isValid= true

            if (endMileage <= 0 )
            {
                isValid= false
                endMileageText.innerHTML = "mileage must be greater than 0"   
            }                
            else
                isValid= true

            if ( startMileage > 0 && endMileage > 0 && endMileage > startMileage)
            {
                isValid= true
                startMileageText.innerHTML = "" 
                endMileageText.innerHTML = ""  
                totalMileage.value = (endMileage - startMileage ).toString()
            }
            else
                isValid= false
                                                        
                                            
        }


        // Enable or disable the save button based on validity
        document.getElementById('save_btn').disabled = !isValid;
        /*if (!isValid)
            document.getElementById('btn btn-success send-btn').style.display = 'none';
        else
            document.getElementsByClassName('btn btn-success send-btn').style.display = 'block';*/
    
        return isValid;
    }
    

}
