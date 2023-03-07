package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // spring framework 를 사용하기 위해
public class HelloController {
    @GetMapping("hello") // 웹 어플리케이션에서 /hello로 들어오면 해당 메서드 호출
    public String hello(Model model) {
        model.addAttribute("data","hello!!");
        // attribute 의 이름이 "data"인 곳에 value 로 "hello!!" 가 들어감
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody // http의 body 부분에 param으로 받은 data를 직접 넣어줌 // view가 필요 없다.
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name; // param으로 받은 게 그대로 요청한 서버에 바로 전달 (name가 spring이면 "hello spring")
    }
}
