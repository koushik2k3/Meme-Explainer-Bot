$(document).ready(function() {
    // Handle navigation clicks
    $('nav a').click(function(e) {
      e.preventDefault();
  
      // Get the target URL from the clicked link
      var targetUrl = $(this).attr('href');
  
      // Use AJAX to load the content of the target URL
      $.ajax({
        url: targetUrl,
        success: function(response) {
          // Update the content container with the loaded content
          $('#content').html(response);
        },
        error: function() {
          // Handle any error during AJAX request
          alert('An error occurred while loading the page.');
        }
      });
  
      // Update the active tab class
      $('nav a').removeClass('active');
      $(this).addClass('active');
    });
  });
  