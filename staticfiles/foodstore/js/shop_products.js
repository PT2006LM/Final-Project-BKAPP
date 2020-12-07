let pageDOM = $('.product__pagination');
let maxNumberVisiblePaginators = 3;

// if totalPages <= maxNumberVisiblePaginators => show all page
if (totalPages <= maxNumberVisiblePaginators) {
    addPaginatorsInRange(0, totalPages);
} else {
    // Check if the page number near the beginnin, i.e: 0
    if (pageNumber <= maxNumberVisiblePaginators / 2) {
        // Show all page from beginning 
        // till the page with number equal to maxNumberVisiblePaginators
        addPaginatorsInRange(0, maxNumberVisiblePaginators)
    } else if (totalPages - pageNumber <= maxNumberVisiblePaginators / 2) {
        // Page number near the end, i.e: totalPages
        // Show all page till the end 
        // with number of pages equal to maxNumberVisiblePaginators
        addPaginatorsInRange(totalPages - maxNumberVisiblePaginators, totalPages);
    } else {
        let currentPagePosition = parseInt(maxNumberVisiblePaginators / 2);
        addPaginatorsInRange(pageNumber - currentPagePosition - 1,
            pageNumber - currentPagePosition - 1 + maxNumberVisiblePaginators);
    }
}

$('select[name=sort_by]').change(function () {
    $('#sort-form').submit();
})

function addPaginatorsInRange(start, end) {
    let firstPageUrl = "{% add_query_params request page=1 %}";
    let startPaginatorString = start === 0 && pageNumber === start + 1 ?
        `<a href="#" class="disabled marker">First</a>` :
        `<a href="${firstPageUrl}" class="marker">First</a>`;
    pageDOM.append(startPaginatorString);

    for (let i = start; i < end; i++) {
        let newPageURL = firstPageUrl.replace(/(page=1)$/, `page=${i + 1}`)
        let newElementString = i === pageNumber - 1 ?
            `<a href="#" class="disabled">${i + 1}</a>` :
            `<a href="${newPageURL}">${i + 1}</a>`;
        pageDOM.append(newElementString);
    }

    let lastPage = totalPages;
    let lastPageURL = firstPageUrl.replace(/(page=1)$/, `page=${lastPage}`)
    let endPaginatorString = end === lastPage && pageNumber === end ?
        `<a href="#" class="disabled marker">Last</a>` :
        `<a href="${lastPageURL}" class="marker">Last</a>`;
    pageDOM.append(endPaginatorString);
}