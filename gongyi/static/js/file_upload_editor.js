/**
 * Created by lihuimin on 15/8/2.
 */

(jQuery || django.jQuery)(function ($) {
    var image_upload = '<div class="fileupload-button"><span class="fileupload-icon"></span>上传<input type="file" id="id_icon_up" multiline="multiline" class="file-input" accept="image/jpeg,image/png,image/bmp"></div>';

    $("#id_icon").parent().append(image_upload);
    $("body").append('<div id="loading" style="display: none;"></div>');


    $(".fileupload-button input[type='file']").change(function (e) {
        var _id = this.id;
        _id = _id.substr(0, _id.length - 3);

        // 直接通过Ajax来提交，避免了iframe的操作 by feiwang@chunyu.me
        var file = e.currentTarget.files[0];

        $("#loading").show();

        //模拟数据
        var fd = new FormData();
        fd.append('file', file, file.name || ('blob.' + file.type.substr('image/'.length)));
        fd.append('type', 'image');
        var xhr = new XMLHttpRequest();
        xhr.open("post", "/gongyi/save_file/", true);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.addEventListener('load', function (e) {
            $("#loading").hide();
            var r = e.target.response;

            try {
                var json = eval('(' + r + ')');
                var url = json.file

                $("#" + _id).val(url);

                $("#" + _id + "_preview").attr("src", url);
                $("#" + _id + "_preview").show();

                //alertify.success("图片上传成功");
            } catch (e) {
                //alertify.success("图片上传失败");
            }
        });
        xhr.send(fd);
    });
});