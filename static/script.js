function getFormData() {
    return {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        custom_note: document.getElementById('customNote').value
    };
}

function previewCard() {
    const data = getFormData();
    
    fetch('/preview', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const previewArea = document.getElementById('previewArea');
            const birthdayCard = previewArea.querySelector('.birthday-card');
            const cardContent = previewArea.querySelector('.card-content');
            const designIcon = previewArea.querySelector('.card-design i');
            
            // Update content and styling
            cardContent.textContent = data.message;
            birthdayCard.className = `birthday-card ${data.background}`;
            designIcon.className = `design-icon design-${data.design}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while previewing the card');
    });
}

function downloadCard() {
    const birthdayCard = document.querySelector('.birthday-card');
    
    // Temporarily modify the card for better image capture
    const originalStyle = {
        width: birthdayCard.style.width,
        height: birthdayCard.style.height,
        transform: birthdayCard.style.transform,
        animation: birthdayCard.style.animation
    };

    // Set optimal dimensions for high-quality image
    birthdayCard.style.width = '800px';
    birthdayCard.style.height = '600px';
    birthdayCard.style.transform = 'none';
    birthdayCard.style.animation = 'none';

    // Add a temporary class for download-specific styling
    birthdayCard.classList.add('download-mode');
    
    html2canvas(birthdayCard, {
        scale: 3, // Increase scale for higher quality
        useCORS: true,
        backgroundColor: null,
        logging: false,
        allowTaint: true,
        foreignObjectRendering: true,
        imageTimeout: 0,
        removeContainer: true,
        letterRendering: true,
        width: 800,
        height: 600
    }).then(canvas => {
        // Restore original styling
        birthdayCard.style.width = originalStyle.width;
        birthdayCard.style.height = originalStyle.height;
        birthdayCard.style.transform = originalStyle.transform;
        birthdayCard.style.animation = originalStyle.animation;
        birthdayCard.classList.remove('download-mode');
        
        // Convert to high-quality PNG
        canvas.toBlob(function(blob) {
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            
            // Get recipient's name for filename
            const recipientName = document.getElementById('name').value;
            const sanitizedName = recipientName.replace(/[^a-z0-9]/gi, '_').toLowerCase();
            const timestamp = new Date().getTime();
            link.download = `birthday_card_${sanitizedName}_${timestamp}.png`;
            
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);
        }, 'image/png', 1.0); // Maximum quality
    }).catch(error => {
        console.error('Error:', error);
        alert('An error occurred while downloading the card');
        
        // Restore original styling in case of error
        birthdayCard.style.width = originalStyle.width;
        birthdayCard.style.height = originalStyle.height;
        birthdayCard.style.transform = originalStyle.transform;
        birthdayCard.style.animation = originalStyle.animation;
        birthdayCard.classList.remove('download-mode');
    });
}

function sendEmail() {
    const data = getFormData();
    
    if (!data.email) {
        alert('Please enter recipient\'s email address');
        return;
    }
    
    fetch('/send_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert('Email sent successfully!');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while sending the email');
    });
}
