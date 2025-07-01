var $value = "all 0.3s ease-in";

$(".formError, input").css("transition", $value);

$("form").on("click", "input#submit", function() {
	$(".formError").css("opacity", "1");
});

$("form").on("keydown", "input,textarea", function() {
	$parent = $(this).parents(".formItem");
	$label = $parent.find("label");
	$label.css("top", "-2px");
	$(this).css("borderRadius", "0 0 5px 5px");

});

$("form").on("blur", "input,textarea", function() {
	$parent = $(this).parents(".formItem");
	$label = $parent.find("label");
	$error = $parent.find(".formError");
	$label.css("top", "15px");
	$error.css("opacity", 0);
	$(this).css("borderRadius", "5px");
});