<?php include('inc/head.inc'); ?>
<style>
  .block-region {
    background: #ccc;
    padding: 2em;
    margin: .25em;
  }

  .region-spotlight {
    padding-top: 0;
  }

  .region-spotlight .block-region {
    padding: 5em;
    margin: 0;
  }

  #breadcrumb {
    display: none;
  }
  #masthead {
    min-height: 160px;
  }
</style>
<body class="front" >
<div id="page">
  <?php include('inc/masthead.inc'); ?>
  <section role="main" id="main" class="with-spotlight">
    <div class="region region-spotlight block-count-0 clearfix">
      <div class="block-region">Spotlight area in header typically used for home page carousels</div>  </div>
    <div class="row clearfix">

      <div id="page-title">
        <h2 class="title">Georgia Tech Regions</h2>
      </div>


      <div id="content-lead">
        <div class="region region-content-lead block-count-0 clearfix">
          <div class="block-region">Area ABOVE Main Content (IGNORES sidebar regions)</div>  </div>
      </div>

      <div class="both-sidebars" id="content">



        <div class="region region-main-top block-count-0 clearfix">
          <div class="block-region">Area ABOVE Main Content (RESPECTS sidebar regions)</div>  </div>
        <div class="region region-content block-count-0 clearfix">
          <div class="block-region">Main Content</div>  </div>
        <div class="region region-main-bottom block-count-0 clearfix">
          <div class="block-region">Area BELOW Main Content (RESPECTS sidebar regions)</div>  </div>
      </div><!-- /#content -->


      <div aria-label="Sidebars" role="complementary">

        <aside id="sidebar-left" class="with-sidebar-right">
          <nav id="left-nav">
            <div class="region region-left-nav block-count-0 clearfix">
              <div class="block-region">Left Side Menu (displays above all other content in Left Sidebar)</div>  </div>
          </nav>
          <div class="region region-left block-count-0 clearfix">
            <div class="block-region">Left Sidebar</div>  </div>
        </aside>

        <aside id="sidebar-right" class="with-sidebar-left">
          <div class="region region-right block-count-0 clearfix">
            <div class="block-region">Right Sidebar</div>  </div>
        </aside>
      </div>

      <div id="content-close">
        <div class="region region-content-close block-count-0 clearfix">
          <div class="block-region">Area BELOW Main Content (IGNORES sidebar regions)</div>  </div>
      </div>

    </div>
  </section>
  <!-- /#main -->

  <?php /* include('inc/superfooter.inc');  */ ?>
  <?php include('inc/footer.inc'); ?>
</div>
<!-- /#page -->

</body>
</html>