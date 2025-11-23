document.addEventListener("DOMContentLoaded", function () {
    // 1. 获取所有带有 lazyload 类的图片
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazyload"));

    // 2. 判断浏览器是否支持 IntersectionObserver (现代浏览器都支持)
    if ("IntersectionObserver" in window) {
        let lazyImageObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                // 如果图片进入可视区域
                if (entry.isIntersecting) {
                    let lazyImage = entry.target;

                    // [核心] 将 data-src 赋值给 src
                    if (lazyImage.dataset.src) {
                        lazyImage.src = lazyImage.dataset.src;
                    }

                    // 移除 lazyload 类，停止动画，停止观察
                    lazyImage.classList.remove("lazyload");
                    lazyImageObserver.unobserve(lazyImage);
                }
            });
        });

        // 开始观察每一个图片
        lazyImages.forEach(function (lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    } else {
        // 3. 兜底方案：如果浏览器太老，直接加载所有图片
        lazyImages.forEach(function (lazyImage) {
            if (lazyImage.dataset.src) {
                lazyImage.src = lazyImage.dataset.src;
                lazyImage.classList.remove("lazyload");
            }
        });
    }
});