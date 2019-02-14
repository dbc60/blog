---
date: 2019-02-14T09:43:00-05:00
description: "A d3js example that alternates shades of gray from one paragraph to the next"
categories: [d3]
tags: [example]
title: "D3 Example: Alternating Shades of Gray"
---

We can have a black background and alternate shades of gray for each paragraph
of the text.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nunc neque, tristique eu scelerisque at, condimentum id turpis. Aliquam erat volutpat. Mauris aliquam nibh tincidunt sem pretium sollicitudin. Suspendisse in vehicula magna. Ut vel gravida tortor, id mattis lacus. Fusce ornare, nisl eu vestibulum ultricies, libero enim semper nisi, ac porta ipsum tortor in nunc. Sed rutrum quam vel felis facilisis pretium. Cras placerat, sapien eget vestibulum tincidunt, odio ipsum efficitur arcu, in laoreet lectus enim sit amet velit. Vivamus ac dolor vitae turpis blandit lobortis. Suspendisse vel tellus felis. Aliquam sodales nisl nec condimentum cursus. Nullam lacinia eu justo quis mattis.

Nullam vitae nisl at lacus sodales tempus. Aliquam a ex sed purus feugiat gravida eget et neque. Phasellus convallis, nunc at condimentum facilisis, urna mauris vulputate diam, sit amet ullamcorper ligula ante eget velit. Mauris eget placerat diam. Aenean interdum, urna a vulputate condimentum, magna sapien finibus nibh, id hendrerit urna nunc eu nibh. Praesent ultrices, nunc sed tincidunt pulvinar, diam libero fermentum arcu, et dignissim mi justo et lacus. Pellentesque in varius enim, ut egestas lacus.

Suspendisse eget nisi felis. Donec tincidunt dolor sit amet mi porta dignissim. Pellentesque pellentesque justo in leo blandit commodo. Mauris sit amet diam et metus egestas commodo. Phasellus venenatis tempus nulla elementum vulputate. Vivamus id interdum tellus. Praesent blandit condimentum sem. Nunc ultricies, risus pharetra accumsan consectetur, sem arcu tincidunt turpis, eu tristique turpis tellus ut erat. Vivamus sit amet urna non enim congue varius. Quisque luctus dui sollicitudin lacus placerat congue. Maecenas ullamcorper nulla orci, sed malesuada felis finibus sit amet. Donec convallis euismod nibh, eu lacinia risus facilisis quis.

Donec dictum sed sapien ut lacinia. Duis nisi mauris, laoreet at arcu maximus, cursus fermentum enim. Suspendisse volutpat eget nulla id tempus. Phasellus imperdiet est at orci varius, eget vehicula nunc semper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin eu bibendum ligula. Praesent tristique massa et gravida egestas. Praesent imperdiet nibh in nibh viverra eleifend non in ante. Morbi viverra nulla risus, in luctus nulla scelerisque maximus. Fusce vel porttitor quam. Suspendisse potenti. Nullam hendrerit erat nec eros semper ultrices. Aliquam sed ornare tortor, vitae facilisis lacus.

Suspendisse euismod ipsum mi, vel ullamcorper purus pellentesque quis. Morbi rutrum finibus justo, ac interdum turpis aliquet ut. Vestibulum faucibus lorem sed massa laoreet, a eleifend tortor ultricies. Sed lacinia pretium justo cursus euismod. Pellentesque ullamcorper metus felis, eget maximus est convallis vitae. Nullam accumsan quis leo nec euismod. Integer vitae varius sapien. Aliquam condimentum rhoncus fringilla. Duis at odio nunc. Etiam aliquet dolor ac nulla lacinia, quis congue nulla dapibus. Morbi at erat sed odio fringilla dapibus sed ut odio. Cras at suscipit lorem. Aliquam in porta urna.

The script is below.

```html
<script>
  d3.select("body").style("background-color", "black");

  d3.selectAll("p").style("color", function(d, i) {
    return i % 2 ? "#fff" : "#ccc";
  });
</script>
```

<script>
  d3.select("body").style("background-color", "black");
  d3.selectAll("p").style("color", function(d, i) {
    return i % 2 ? "#fff" : "#ccc";
  });
</script>
