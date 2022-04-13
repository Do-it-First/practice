import { FunctionComponent, useCallback } from "react";
import styles from "./css/Desktop11.module.css";

export const Desktop11: FunctionComponent = () => {
  const onTextClick = useCallback(() => {
    window.open("다른작품화면");
  }, []);

  const onRectangleClick = useCallback(() => {
    window.open("다른작품화면");
  }, []);

  const onContainer5Click = useCallback(() => {
    window.open("공식플랫폼");
  }, []);

  const onText7Click = useCallback(() => {
    window.open(
      "https://www.figma.com/file/2P3p4u9jLwLlTIpHbhbO3t/?node-id=0%3A1"
    );
  }, []);

  return (
    <div className={styles.desktop1}>
      <div className={styles.groupDiv}>
        <div className={styles.div}>
          <div className={styles.div1} onClick={onTextClick}>
            작품명
          </div>
          <div className={styles.div2} onClick={onRectangleClick} />
        </div>
        <img className={styles.icon} alt="" src=".svg" />
        <img className={styles.icon1} alt="" src="1.svg" />
        <img className={styles.icon2} alt="" src="2.svg" />
        <div className={styles.div3}>유사 작품 추천</div>
      </div>
      <div className={styles.div4}>
        <div className={styles.div5} />
        <div className={styles.div6}>작품 소개</div>
      </div>
      <a className={styles.a}>
        <b className={styles.b}>작품명</b>
        <div className={styles.div7}>작가</div>
        <div className={styles.div8}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv}>키워드1</div>
        </div>
        <div className={styles.div9}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv1}>키워드2</div>
        </div>
        <div className={styles.div10}>
          <div className={styles.rectangleDiv2} />
          <div className={styles.div11}>플랫폼</div>
        </div>
        <div className={styles.div12} onClick={onContainer5Click}>
          <div className={styles.rectangleDiv3} />
          <div className={styles.div13}>웹툰 감상하기</div>
        </div>
        <div className={styles.div14} />
      </a>
      <div className={styles.div15}>
        <div className={styles.rectangleDiv4} />
      </div>
      <div className={styles.div16} onClick={onText7Click}>
        <p className={styles.p}>일단해보조</p>
        <p className={styles.p1}>웹툰 통합플랫폼</p>
      </div>
    </div>
  );
};
