import { BallCanvas } from "./canvas";
import { SectionWrapper } from "../hoc";
import { technologies } from "../constants";

const Tech = () => {
  return (
    <div className="flex flex-row flex-wrap justify-center gap-10">
      {technologies.map((technoLogy) => (
        <div className="w-28 h-28" key={technoLogy.name}>
          <BallCanvas icon={technoLogy.icon} />
        </div>
    ))}
    </div>
  )
}

export default SectionWrapper(Tech, "");