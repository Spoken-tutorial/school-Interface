import React from "react";
import Announcements from "./Announcements/Announcements";
import HeroSection from "./HeroSection/HeroSection";
import Awards from "./Awards/Awards";
import FeedbackCollaborate from "./FeedbackCollaborate/FeedbackCollaborate.jsx";
import CommunityInsights from "./CommunityInsights/CommunityInsights.jsx";
import Testimonials from "./Testimonials/Testimonials.jsx";
function Home() {
  return (
    <>
      <Announcements />
      <HeroSection />
      <Awards />
      <CommunityInsights />
      <Testimonials />
      <FeedbackCollaborate />
    </>
  );
}

export default Home;
