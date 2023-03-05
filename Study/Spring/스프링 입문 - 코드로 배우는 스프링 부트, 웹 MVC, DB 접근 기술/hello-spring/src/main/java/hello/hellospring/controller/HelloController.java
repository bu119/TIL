package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller // spring framework 를 사용하기 위해
public class HelloController {
    @GetMapping("hello") // 웹 어플리케이션에서 /hello로 들어오면 해당 메서드 호출
    public String hello(Model model) {
        model.addAttribute("data","hello!!");
        // attribute 의 이름이 "data"인 곳에 value 로 "hello!!" 가 들어감
        return "hello";
    }

}
