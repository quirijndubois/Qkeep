textareas = document.querySelectorAll("textarea");
textareas.forEach((textarea) => {
    const updateHeight = () => {
        let lines = textarea.value.split("\n").length;
        textarea.style.height = (lines * 1.5) + "em";
    };

    updateHeight();
    textarea.addEventListener("input", updateHeight);
});
